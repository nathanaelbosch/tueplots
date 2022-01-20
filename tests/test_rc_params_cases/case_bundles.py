"""Test cases for bundles."""

import pytest_cases

from tueplots import bundles


@pytest_cases.parametrize(column=["full", "half"])
@pytest_cases.parametrize(usetex=[True, False])
def case_bundles_icml2022(column, usetex):
    return bundles.icml2022(
        nrows=2, ncols=2, family="serif", column=column, usetex=usetex
    )


def case_bundles_jmlr2001_tex():
    return bundles.jmlr2001_tex(nrows=2, ncols=2, family="serif")


@pytest_cases.parametrize(column=["full", "half"])
def case_bundles_aistats2022(column):
    return bundles.aistats2022_tex(column=column, nrows=2, ncols=2, family="serif")


@pytest_cases.parametrize(usetex=[True, False])
def case_bundles_neurips2021(usetex):
    return bundles.neurips2021(usetex=usetex, nrows=2, ncols=2, family="serif")


def case_bundles_beamer_moml_tex():
    return bundles.beamer_moml(rel_width=0.9, rel_height=0.9)


def case_bundles_beamer_moml_dark_bg_tex():
    return bundles.beamer_moml(rel_width=0.9, rel_height=0.9)
