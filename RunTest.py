import unittest
from run.run_test_trade import RunOpenCloud
from BeautifulReport import BeautifulReport

if __name__ == '__main__':
    cases = unittest.TestSuite()
    cases.addTest(unittest.makeSuite(RunOpenCloud))
    result = BeautifulReport(cases)
    result.report(filename="TestReport", description="Test Report", report_dir="report", theme="theme_default")
