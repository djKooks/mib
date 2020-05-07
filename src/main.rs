#[macro_use]
extern crate clap;
use clap::{App, AppSettings, Arg};

use clipboard::ClipboardContext;
use clipboard::ClipboardProvider;

fn main() {
    let app = App::new(crate_name!())
        .version(crate_version!())
        .about("0.0.1")
        .author("kwangin.jung");

    // Define the name command line option
    let key_option = Arg::with_name("key").about("Key of Set").required(true);

    let value_option = Arg::with_name("value")
        .takes_value(true)
        .about("value of Set")
        .required(true);

    let put_command = App::new("put")
        .about("put data in kv")
        .arg(key_option)
        .arg(value_option);
    // now add in the argument we want to parse
    let app = app.subcommand(put_command);

    // extract the matches
    // let matches = app.get_matches();
    // let name = matches
    // .value_of("value")
    // .expect("This can't be None, we said it was required");

    // println!("Hello, {}!", name);

    // let mut ctx: ClipboardContext = ClipboardProvider::new().unwrap();
    // println!("{:?}", ctx.get_contents());
    // ctx.set_contents("some string".to_owned()).unwrap();
}
