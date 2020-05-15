use bawikv::BawiKv;
use bawikv::{InternalError, Result};
use std::error::Error;
use std::path::Path;

pub struct Store {
    bdb: BawiKv,
}

impl Store {
    /// TODO: new
    pub fn new() -> Store {
        let path = Path::new("rote_store");
        let bdb = BawiKv::open(path).unwrap();
        Store { bdb }
    }
    /// TODO: get
    pub fn get(&mut self, key: String) -> Result<String> {
        let value = self.bdb.get(key)?;
        if let Some(val) = value {
            return Ok(val);
        } else {
            return Err(InternalError::Unexpected);
        }
    }
    /// TODO: put
    pub fn put(&mut self, key: String, value: String) -> Result<()> {
        self.bdb.put(key, value);
        Ok(())
    }
    /// TODO: find_by_key
    fn find_by_key(key: &str) -> &str {
        /// TODO
        "find value"
    }
}
