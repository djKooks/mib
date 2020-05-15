#[macro_use]
extern crate clap;
pub mod cli;
pub mod store;

pub use cli::cli;
pub use store::Store;

fn main() {
    cli();
}
