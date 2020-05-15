use clap::{App, Arg};

use clipboard::ClipboardContext;
use clipboard::ClipboardProvider;

use crate::Store;

pub fn cli() {
  let app = App::new(crate_name!())
    .version(crate_version!())
    .about("terminal-based text storage based on key-value")
    .author("dennis.jung");

  // Define the name command line option
  let key_option = Arg::with_name("key")
    .about("Key of Set")
    .required(true)
    .index(1);

  let value_option = Arg::with_name("value")
    .about("value of Set")
    .required(true)
    .index(2);

  let put_command = App::new("put")
    .about("put data in kv")
    .arg(key_option)
    .arg(value_option);
  // now add in the argument we want to parse
  // extract the matches
  let store = Store::new();

  let matches = app.subcommand(put_command).get_matches();
  if let Some(matches) = matches.subcommand_matches("put") {
    if let Some(key) = matches.value_of("key") {
      println!("Printing key: {}", key);
    }
    if let Some(value) = matches.value_of("value") {
      println!("Printing value: {}", value);
    }
  }

  println!("Done!");

  // let mut ctx: ClipboardContext = ClipboardProvider::new().unwrap();
  // println!("{:?}", ctx.get_contents());
  // ctx.set_contents("some string".to_owned()).unwrap();
}
