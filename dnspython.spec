#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : dnspython
Version  : 1.15.0
Release  : 41
URL      : http://pypi.debian.net/dnspython/dnspython-1.15.0.zip
Source0  : http://pypi.debian.net/dnspython/dnspython-1.15.0.zip
Summary  : DNS toolkit
Group    : Development/Tools
License  : ISC
Requires: dnspython-python3
Requires: dnspython-python
BuildRequires : pbr
BuildRequires : pip

BuildRequires : python3-dev
BuildRequires : setuptools

%description
record types. It can be used for queries, zone transfers, and dynamic
        updates.  It supports TSIG authenticated messages and EDNS0.
        
        dnspython provides both high and low level access to DNS. The high
        level classes perform queries for data of a given name, type, and
        class, and return an answer set.  The low level classes allow
        direct manipulation of DNS zones, messages, names, and records.

%package python
Summary: python components for the dnspython package.
Group: Default
Requires: dnspython-python3

%description python
python components for the dnspython package.


%package python3
Summary: python3 components for the dnspython package.
Group: Default
Requires: python3-core

%description python3
python3 components for the dnspython package.


%prep
%setup -q -n dnspython-1.15.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1523288206
python3 setup.py build -b py3

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
cd tests ; make test
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
