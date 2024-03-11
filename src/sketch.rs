use serde::{Deserialize, Serialize};

#[derive(Debug, Deserialize, Serialize)]
pub struct Hymn {
    pub id: u32,
    author: String,
    pub starts: String,
    pub chorus: Vec<String>,
    bridge: Vec<String>,
    pub verses: Vec<Vec<String>>,
}

#[derive(Debug)]
pub enum Hymnary {
    Single(Hymn),
    Multiple(Vec<Hymn>),
}
