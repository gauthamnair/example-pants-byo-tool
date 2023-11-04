from pants.backend.adhoc.code_quality_tool import CodeQualityToolRuleBuilder

confs = [
    CodeQualityToolRuleBuilder(
        goal="lint", target="//:flake8_linter", scope="flake8", name="Flake8"
    ),
    CodeQualityToolRuleBuilder(
        goal="lint",
        target="//:markdownlint_linter",
        scope="markdownlint",
        name="Markdown Lint",
    ),
    CodeQualityToolRuleBuilder(
        goal="fmt", target="//:black_formatter", scope="black_tool", name="Black"
    ),
]


def rules():
    rules = []
    for cfg in confs:
        rules.extend(cfg.rules())
    return rules
