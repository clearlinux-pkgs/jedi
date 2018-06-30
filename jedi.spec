#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : jedi
Version  : 0.12.0
Release  : 19
URL      : http://pypi.debian.net/jedi/jedi-0.12.0.tar.gz
Source0  : http://pypi.debian.net/jedi/jedi-0.12.0.tar.gz
Summary  : An autocompletion tool for Python that can be used for text editors.
Group    : Development/Tools
License  : BSD-3-Clause MIT
Requires: jedi-python3
Requires: jedi-python
Requires: parso
BuildRequires : parso
BuildRequires : pbr
BuildRequires : pip
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pytest

BuildRequires : python3-dev
BuildRequires : setuptools
BuildRequires : tox
BuildRequires : virtualenv

%description
Jedi - an awesome autocompletion/static analysis library for Python
        ###################################################################

%package python
Summary: python components for the jedi package.
Group: Default
Requires: jedi-python3

%description python
python components for the jedi package.


%package python3
Summary: python3 components for the jedi package.
Group: Default
Requires: python3-core

%description python3
python3 components for the jedi package.


%prep
%setup -q -n jedi-0.12.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1523855671
python3 setup.py build -b py3

%install
rm -rf %{buildroot}
python3 -tt setup.py build -b py3 install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
