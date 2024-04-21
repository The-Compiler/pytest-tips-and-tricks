import pytest
import pytest_mock

from rpncalc.utils import Config
from rpncalc.rpn_v3 import RPNCalculator
from rpncalc.convert import Converter


@pytest.fixture
def rpn(mocker: pytest_mock.MockerFixture) -> RPNCalculator:
    mock = mocker.Mock(spec=Converter)
    mock.eur2chf.return_value = 20
    mock.chf2eur.return_value = 5
    return RPNCalculator(config=Config(), converter=mock)

def test_convert(rpn: RPNCalculator):
    rpn.stack = [10]
    rpn.evaluate("eur2chf")
    assert rpn.stack == [20]

    rpn.converter.eur2chf.assert_called_once_with(10)
