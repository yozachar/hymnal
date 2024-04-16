use std::{
    env,
    fs::{create_dir_all, read_dir},
    io::{BufRead, BufReader},
    path::{Path, PathBuf},
    process::{Command, Stdio},
};

mod populate;
mod sketch;
mod transform;
mod utility;

fn is_directory_empty(dir_path: PathBuf) -> bool {
    if let Ok(entries) = read_dir(dir_path) {
        entries.count() == 0
    } else {
        false
    }
}

pub fn exec_stream<P: AsRef<Path>>(binary: P, args: Vec<&str>) {
    // refer: https://stackoverflow.com/a/50444713/8828460
    let mut cmd = Command::new(binary.as_ref())
        .args(&args)
        .stdout(Stdio::piped())
        .spawn()
        .unwrap();

    {
        let stdout = cmd.stdout.as_mut().unwrap();
        let stdout_reader = BufReader::new(stdout);
        let stdout_lines = stdout_reader.lines();

        for line in stdout_lines {
            println!("{}", line.unwrap());
        }
    }

    cmd.wait().unwrap();
}

fn prepare() {
    println!();
    let current_dir = env::current_dir()
        .expect(format!("E@{}: Unable to read current directory", line!()).as_str());
    let lib_dir = current_dir.join("static/lib/reveal.js");
    create_dir_all(lib_dir.clone()).unwrap();
    let lib_dir_temp = lib_dir.clone();
    let lib_dir_str = lib_dir_temp.to_str().unwrap();

    let lib_src_url = "https://github.com/hakimel/reveal.js.git";

    if is_directory_empty(lib_dir.clone()) {
        exec_stream(
            "git",
            vec!["clone", "--depth", "1", lib_src_url, lib_dir_str],
        );
    } else {
        exec_stream("git", vec!["-C", lib_dir_str, "pull", lib_src_url]);
    }
}

fn main() {
    prepare();
    populate::ensconce();
    transform::alter();
}
