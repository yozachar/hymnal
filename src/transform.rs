use crate::sketch::{Hymn, Hymnary};
use crate::utility::{read_from_json_file, write_to_html_file, zfill};
use minijinja::{context, filters::safe, path_loader, Environment};
use std::{env, fs::create_dir_all, path::PathBuf};

fn render_html(hymn: Hymn, jinja: Environment) -> String {
    // hymnal.sort_by_key(|item| (item.id));
    // println!("{:#?}", hymnal);
    // for song in hymnal {}

    let song_template = match (
        hymn.starts.as_str(),
        hymn.chorus.is_empty(),
        hymn.verses.is_empty(),
    ) {
        ("chorus", false, false) => "starts-at-chorus-with-verses.html.j2",
        ("chorus", false, true) => "starts-at-chorus-without-verses.html.j2",
        ("verse-1", false, false) => "starts-at-verse-with-chorus.html.j2",
        ("verse-1", true, false) => "starts-at-verse-without-chorus.html.j2",
        _ => "",
    };

    if song_template.is_empty() {
        // try printing the song number if this happens
        panic!("E@{}: Song template cannot be empty", line!())
    }

    let fvc = if !hymn.verses.is_empty() {
        context! { first_verse => hymn.verses[0] }
    } else {
        context! {}
    };

    let render_context = context! {
        hymn_number => hymn.id,
        hymnal_name => "ആത്മീയ ഗീതങ്ങൾ",
        relative_path => safe("../..".to_string()),
        verses => if hymn.starts == "chorus" {hymn.verses} else {hymn.verses[1..].to_vec()},
        chorus => hymn.chorus,
        ..fvc,
    };

    jinja
        .get_template(song_template)
        .expect("E: Template not found")
        .render(render_context)
        .expect("E: JSON to HTML render failed")
}

fn j2h_transform(hymnal: Vec<Hymn>, current_dir: PathBuf) {
    let template_dir = current_dir.join("src/jinja");
    let mut jinja_env = Environment::new();
    jinja_env.set_loader(path_loader(template_dir));
    // jinja_env.add_filter(name, f)

    let target_dir = current_dir.join("static/g11n/mal");
    create_dir_all(target_dir.clone()).unwrap();

    for (idx, hymn) in hymnal.into_iter().enumerate() {
        let _ = idx;
        let file_name = zfill(hymn.id.to_string(), 7);
        write_to_html_file(
            target_dir.join(format!("{file_name}.html")),
            render_html(hymn, jinja_env.clone()),
        );
        print!("Writing file: {}.html\r", file_name);
    }
    println!("\nDone.")
}

pub fn alter() {
    println!();
    let cur_dir = env::current_dir()
        .expect(format!("E@{}: Unable to read current directory", line!()).as_str());
    let json_source_file = cur_dir.join("db/lyrics.mal.db.json");
    // let json_target_file = cur_dir.join("test.json"); //"db/lyrics.mal.db.json"
    // write_to_json_file(json_target_file, read_from_json_file(json_source_file))
    if let Hymnary::Multiple(hymnal) = read_from_json_file(json_source_file) {
        j2h_transform(hymnal, cur_dir)
    }
}
