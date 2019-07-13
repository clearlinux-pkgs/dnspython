#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xF24B3AFC8CA2F5C7 (halley@dnspython.org)
#
Name     : dnspython
Version  : 1.16.0
Release  : 47
URL      : https://files.pythonhosted.org/packages/ec/c5/14bcd63cb6d06092a004793399ec395405edf97c2301dfdc146dfbd5beed/dnspython-1.16.0.zip
Source0  : https://files.pythonhosted.org/packages/ec/c5/14bcd63cb6d06092a004793399ec395405edf97c2301dfdc146dfbd5beed/dnspython-1.16.0.zip
Source99 : https://files.pythonhosted.org/packages/ec/c5/14bcd63cb6d06092a004793399ec395405edf97c2301dfdc146dfbd5beed/dnspython-1.16.0.zip.asc
Summary  : DNS toolkit
Group    : Development/Tools
License  : ISC
Requires: dnspython-license = %{version}-%{release}
Requires: dnspython-python = %{version}-%{release}
Requires: dnspython-python3 = %{version}-%{release}
Requires: ecdsa
Requires: idna
BuildRequires : buildreq-distutils3

%description
record types. It can be used for queries, zone transfers, and dynamic
        updates.  It supports TSIG authenticated messages and EDNS0.
        
        dnspython provides both high and low level access to DNS. The high
        level classes perform queries for data of a given name, type, and
        class, and return an answer set.  The low level classes allow
        direct manipulation of DNS zones, messages, names, and records.

%package license
Summary: license components for the dnspython package.
Group: Default

%description license
license components for the dnspython package.


%package python
Summary: python components for the dnspython package.
Group: Default
Requires: dnspython-python3 = %{version}-%{release}

%description python
python components for the dnspython package.


%package python3
Summary: python3 components for the dnspython package.
Group: Default
Requires: python3-core

%description python3
python3 components for the dnspython package.


%prep
%setup -q -n dnspython-1.16.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1545509340
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
cd tests ; make test
%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/dnspython
cp LICENSE %{buildroot}/usr/share/package-licenses/dnspython/LICENSE
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/dnspython/LICENSE

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
