#
# Conditional build:
%bcond_without  python2         # Python 2.x module
%bcond_without  python3         # Python 3.x module
#
%define		module		simplejson
Summary:	Simple, fast, extensible JSON encoder/decoder for Python
Summary(pl.UTF-8):	Prosty, szybki, rozszerzalny (de)koder JSON dla Pythona
Name:		python-%{module}
Version:	3.8.0
Release:	1
License:	MIT or AFL v2.1
Group:		Libraries
#Source0Download: https://pypi.python.org/pypi/simplejson
Source0:	https://pypi.python.org/packages/source/s/simplejson/%{module}-%{version}.tar.gz
# Source0-md5:	72f3b93a6f9808df81535f79e79565a2
URL:		http://simplejson.readthedocs.org/
%if %{with python2}
BuildRequires:	python >= 1:2.5
BuildRequires:	python-devel >= 1:2.5
BuildRequires:	python-setuptools >= 0.6-0.c1
%endif
%if %{with python3}
BuildRequires:	python3 >= 1:3.3
BuildRequires:	python3-devel >= 1:3.3
%endif
BuildRequires:	rpm-pythonprov
%pyrequires_eq	python-libs
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
simplejson is a simple, fast, complete, correct and extensible JSON
<http://json.org/> encoder and decoder for Python 2.5+.

%description -l pl.UTF-8
simplejson to prosty, szybki, pełny, poprawny i rozszerzalny koder i
dekoder JSON (<http://json.org/>) dla Pythona 2.5 i nowszych wersji.

%package -n python3-%{module}
Summary:	Simple, fast, extensible JSON encoder/decoder for Python 3
Summary(pl.UTF-8):	Prosty, szybki, rozszerzalny (de)koder JSON dla Pythona 3
Group:		Libraries

%description -n python3-%{module}
simplejson is a simple, fast, complete, correct and extensible JSON
<http://json.org/> encoder and decoder for Python 3.

%description -n python3-%{module} -l pl.UTF-8
simplejson to prosty, szybki, pełny, poprawny i rozszerzalny koder i
dekoder JSON (<http://json.org/>) dla Pythona 3.

%prep
%setup -qn %{module}-%{version}

%build
%if %{with python2}
%py_build --build-base py2
%endif

%if %{with python3}
%py3_build --build-base py3
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%{__python} setup.py \
	build --build-base py2 \
	install \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

rm -rf $RPM_BUILD_ROOT%{py_sitedir}/simplejson/tests
%py_postclean
%endif

%if %{with python3}
%{__python3} setup.py \
	build --build-base py3 \
	install \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

rm -rf $RPM_BUILD_ROOT%{py3_sitedir}/simplejson/tests
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc CHANGES.txt LICENSE.txt README.rst
%dir %{py_sitedir}/simplejson
%{py_sitedir}/simplejson/*.py[co]
%attr(755,root,root) %{py_sitedir}/simplejson/_speedups.so
%{py_sitedir}/simplejson-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-%{module}
%defattr(644,root,root,755)
%dir %{py3_sitedir}/simplejson
%{py3_sitedir}/simplejson/__pycache__
%{py3_sitedir}/simplejson/*.py
%attr(755,root,root) %{py3_sitedir}/simplejson/_speedups.cpython-*.so
%{py3_sitedir}/simplejson-%{version}-py*.egg-info
%endif
