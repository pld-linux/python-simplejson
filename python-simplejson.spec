# TODO: optflags
%define		module		simplejson
Summary:	Simple, fast, extensible JSON encoder/decoder for Python
Summary(pl.UTF-8):	Prosty, szybki, rozszerzalny (de)koder JSON dla Pythona
Name:		python-%{module}
Version:	2.1.2
Release:	1
License:	MIT
Group:		Libraries
Source0:	http://pypi.python.org/packages/source/s/%{module}/%{module}-%{version}.tar.gz
# Source0-md5:	a856f9ae9ab3749991a93ddeafadc554
URL:		http://undefined.org/python/#simplejson
BuildRequires:	python >= 1:2.4
BuildRequires:	python-setuptools >= 0.6-0.c1
BuildRequires:	rpm-pythonprov
%pyrequires_eq	python-libs
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
simplejson is a simple, fast, complete, correct and extensible JSON
<http://json.org/> encoder and decoder for Python 2.4+.

%description -l pl.UTF-8
simplejson to prosty, szybki, pełny, poprawny i rozszerzalny koder i
dekoder JSON (<http://json.org/>) dla Pythona 2.4 i nowszych wersji.

%prep
%setup -qn %{module}-%{version}

%build
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT

%{__python} setup.py install \
	--root=$RPM_BUILD_ROOT \
	--optimize=2

%py_postclean
rm -rf $RPM_BUILD_ROOT%{py_sitedir}/simplejson/tests

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{py_sitedir}/simplejson
%{py_sitedir}/simplejson/*.py[co]
%attr(755,root,root) %{py_sitedir}/simplejson/*.so
%{py_sitedir}/simplejson-%{version}-py*.egg-info
