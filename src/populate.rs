use crate::sketch::{Hymn, Hymnary};
use crate::utility::{read_from_json_file, write_to_json_file};
use std::{
    env,
    fs::{create_dir_all, read_dir},
    path::PathBuf,
};

fn generate(given_dir: PathBuf) -> Vec<Hymn> {
    let mut json_array: Vec<Hymn> = Vec::new();
    let paths = read_dir(given_dir)
        .expect(format!("E@{}: Unable to find given directory", line!()).as_str());

    // Iterate through each entry in the directory
    for path in paths {
        // Unwrap the directory entry
        let entry = path.expect(format!("E@{}: Unable to open sub-directory", line!()).as_str());
        let file_path = entry.path();
        let file_name = entry.file_name().into_string().unwrap();
        print!("Reading file: {file_name}\r");
        // let white_space = " ".repeat(30);
        if let Hymnary::Single(hymn) = read_from_json_file(file_path) {
            json_array.push(hymn);
        }
    }
    println!("\nDone.");
    json_array
}

pub fn ensconce() {
    println!();
    let cur_dir = env::current_dir()
        .expect(format!("E@{}: Unable to read current directory", line!()).as_str());

    let lyrics_dir_stub = "data/lyrics/mal";
    let json_data = generate(cur_dir.join(lyrics_dir_stub));

    let json_data = Hymnary::Multiple(json_data);
    let lyrics_db_dir = cur_dir.join("db");
    create_dir_all(lyrics_db_dir.clone()).unwrap();
    write_to_json_file(lyrics_db_dir.join("lyrics.mal.db.json"), json_data);
}
