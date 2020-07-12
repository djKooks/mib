#[macro_use]
extern crate clap;
pub mod cli;
pub mod commands;
pub mod store;

pub use cli::cli;
pub use commands::{get_cmd, put_cmd};
pub use store::Store;

fn main() {
    cli();
}
