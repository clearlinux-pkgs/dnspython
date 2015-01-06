#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : dnspython
Version  : 1.12.0
Release  : 14
URL      : https://pypi.python.org/packages/source/d/dnspython/dnspython-1.12.0.zip
Source0  : https://pypi.python.org/packages/source/d/dnspython/dnspython-1.12.0.zip
Summary  : DNS toolkit
Group    : Development/Tools
License  : ISC
Requires: dnspython-python
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : setuptools

%description
dnspython
INTRODUCTION
dnspython is a DNS toolkit for Python. It supports almost all record
types. It can be used for queries, zone transfers, and dynamic
updates.  It supports TSIG authenticated messages and EDNS0.

%package python
Summary: python components for the dnspython package.
Group: Default

%description python
python components for the dnspython package.


%prep
%setup -q -n dnspython-1.12.0

%build
python2 setup.py build -b py2

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=intel.com,localhost
cd tests ; make test
%install
rm -rf %{buildroot}
python2 setup.py build -b py2 install --root=%{buildroot}

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
