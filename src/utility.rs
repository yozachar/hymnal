use crate::sketch::{Hymn, Hymnary};
use serde_json;
use std::{
    fs::File,
    io::{Read, Write},
    path::PathBuf,
};

pub fn read_from_json_file(source_file: PathBuf) -> Hymnary {
    let mut json_string = String::new();
    let mut json_file = File::open(source_file)
        .expect(format!("E@{}: Unable to open source file", line!()).as_str());
    json_file
        .read_to_string(&mut json_string)
        .expect(format!("E@{}: Unable to read file", line!()).as_str());
    if json_string.starts_with("{") {
        let hymn: Hymn = serde_json::from_str(&json_string)
            .expect(format!("E@{}: Unable to deserialize JSON", line!()).as_str());
        return Hymnary::Single(hymn);
    }
    let hymnal: Vec<Hymn> = serde_json::from_str(&json_string)
        .expect(format!("E@{}: Unable to deserialize JSON", line!()).as_str());
    Hymnary::Multiple(hymnal)
}

pub fn write_to_json_file(target_file: PathBuf, json_data: Hymnary) {
    let mut json_string = String::new();
    if let Hymnary::Single(hymn) = &json_data {
        json_string = serde_json::to_string(&hymn)
            .expect(format!("E@{}: Unable to parse JSON", line!()).as_str());
    }
    if let Hymnary::Multiple(hymnal) = json_data {
        json_string = serde_json::to_string(&hymnal)
            .expect(format!("E@{}: Unable to parse JSON", line!()).as_str());
    }
    let mut file = File::create(target_file.clone()).expect(
        format!(
            "E@{}: Unable to create file at {}",
            line!(),
            target_file.display()
        )
        .as_str(),
    );
    file.write_all(json_string.as_bytes())
        .expect(format!("E@{}: Unable to write to JSON file", line!()).as_str());
}

pub fn write_to_html_file(target_file: PathBuf, html_data: String) {
    let mut file = File::create(target_file.clone()).expect(
        format!(
            "E@{}: Unable to create file at {}",
            line!(),
            target_file.display()
        )
        .as_str(),
    );
    file.write_all(html_data.as_bytes())
        .expect(format!("E@{}: Unable to write to HTML file", line!()).as_str());
}

pub fn zfill(character: String, length: usize) -> String {
    let zeros_to_add = length.saturating_sub(character.len());
    format!("{}{}", "0".repeat(zeros_to_add), character)
}
