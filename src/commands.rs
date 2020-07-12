use clap::{App, Arg};

pub fn put_cmd() -> App<'static> {
    return App::new("put")
        .about("put data in kv")
        .arg(
            Arg::with_name("key")
                .about("Key of Set")
                .required(true)
                .index(1),
        )
        .arg(
            Arg::with_name("value")
                .about("value of Set")
                .required(true)
                .index(2),
        );
}

pub fn get_cmd() -> App<'static> {
    App::new("get").about("get value from kv").arg(
        Arg::with_name("key")
            .about("Key of Set")
            .required(true)
            .index(1),
    )
}
