
from oo_analyzer.inputs import InputData
from oo_analyzer.processor import Processor
from oo_analyzer.analyzers import LengthAnalyzer, UppercaseAnalyzer

def run_metrics(x):
    p = Processor([LengthAnalyzer(), UppercaseAnalyzer()])
    return p.run(InputData(x))

def test_string_case():
    assert run_metrics("Hello NZ") == {"total_length": 8, "uppercase_chars": 3}

def test_list_case():
    assert run_metrics(["Hello","Yoobee","NZ"]) == {"total_length": 3, "uppercase_chars": 3}
