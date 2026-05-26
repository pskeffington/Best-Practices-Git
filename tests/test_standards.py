from best_practices_git.standards import default_mappings, default_standards


def test_default_standards_are_named():
    standards = default_standards()

    assert standards
    assert all(standard.name for standard in standards)


def test_default_mappings_have_reporting_functions():
    mappings = default_mappings()

    assert mappings
    assert all(mapping.has_reporting_function() for mapping in mappings)


def test_default_mappings_have_standards():
    mappings = default_mappings()

    assert all(mapping.standard_names() for mapping in mappings)
