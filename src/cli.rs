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

  let get_key_option = Arg::with_name("key")
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

  let get_command = App::new("get").about("value of Set").arg(get_key_option);
  // now add in the argument we want to parse
  // extract the matches
  let mut store = Store::new();

  let matches = app
    .subcommand(put_command)
    .subcommand(get_command)
    .get_matches();
  if let Some(matches) = matches.subcommand_matches("put") {
    if let Some(key) = matches.value_of("key") {
      println!("Printing key: {}", key);
    }
    if let Some(value) = matches.value_of("value") {
      println!("Printing value: {}", value);
    }
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
