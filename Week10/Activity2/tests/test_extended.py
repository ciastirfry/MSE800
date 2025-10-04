
from oo_analyzer.inputs import InputData
from oo_analyzer.processor import Processor
from oo_analyzer.analyzers import LengthAnalyzer, UppercaseAnalyzer, DigitAnalyzer, SpecialCharAnalyzer

def run_metrics(x):
    p = Processor([LengthAnalyzer(), UppercaseAnalyzer(), DigitAnalyzer(), SpecialCharAnalyzer()])
    return p.run(InputData(x))

def test_string_case():
    s = "Hello NZ 2025! @Yoobee#"
    res = run_metrics(s)
    assert res["total_length"] == len(s)
    assert res["uppercase_chars"] == 4
    assert res["digits"] == 4
    assert res["special_chars"] >= 3

def test_list_case():
    res = run_metrics(["Hi!","NZ-2025","Yoobee :)"])
    assert res["total_length"] == 3
    assert res["digits"] == 4
    assert res["special_chars"] >= 3
