def pytest_report_header() -> list[str]:
    return ["extrainfo: line 1"]


def pytest_terminal_summary(terminalreporter) -> None:
    if terminalreporter.verbosity >= 1:
        terminalreporter.section("my special section")
        terminalreporter.line("report something here")
