use clap::{App, Arg};

use clipboard::ClipboardContext;
use clipboard::ClipboardProvider;

use crate::commands::{get_cmd, put_cmd};

use crate::Store;

pub fn cli() {
  let app = App::new(crate_name!())
    .version(crate_version!())
    .author("dennis.jung<inylove82@gmail.com>")
    .about("terminal-based text storage based on key-value");
  // now add in the argument we want to parse
  // extract the matches
  let mut store = Store::new();

  let matches = app
    .subcommand(put_cmd())
    .subcommand(get_cmd())
    .get_matches();

  if let Some(matches) = matches.subcommand_matches("put") {
    let key = matches.value_of("key").unwrap();
    let value = matches.value_of("value").unwrap();
    store.put(String::from(key), String::from(value));
  }

  if let Some(matches) = matches.subcommand_matches("get") {
    if let Some(key) = matches.value_of("key") {
      let value = store.get(String::from(key)).unwrap();
      println!("get value from key: {}", value);
    }
  }

  println!("Done!");

  // let mut ctx: ClipboardContext = ClipboardProvider::new().unwrap();
  // println!("{:?}", ctx.get_contents());
  // ctx.set_contents("some string".to_owned()).unwrap();
}
