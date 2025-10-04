
from oo_analyzer.inputs import InputData
from oo_analyzer.processor import Processor
from oo_analyzer.analyzers import LengthAnalyzer, UppercaseAnalyzer
proc = Processor([LengthAnalyzer(), UppercaseAnalyzer()])
print("String example:", proc.run(InputData("Hello World! YNZ")))
print("List example:", proc.run(InputData(["Hello","Yoobee","NZ"])))
