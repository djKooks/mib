from click.testing import CliRunner
from laconic.main import init

def test_hello_world():
  runner = CliRunner()
  result = runner.invoke(init, [])
  
