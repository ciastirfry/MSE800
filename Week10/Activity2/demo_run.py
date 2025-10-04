
from oo_analyzer.inputs import InputData
from oo_analyzer.processor import Processor
from oo_analyzer.analyzers import LengthAnalyzer, UppercaseAnalyzer, DigitAnalyzer, SpecialCharAnalyzer

proc = Processor([LengthAnalyzer(), UppercaseAnalyzer(), DigitAnalyzer(), SpecialCharAnalyzer()])

print("String example:", proc.run(InputData("Hello NZ 2025! @Yoobee#")))
print("List example:", proc.run(InputData(["Hi!","NZ-2025","Yoobee :)"])))
