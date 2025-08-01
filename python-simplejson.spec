#
# Conditional build:
%bcond_without	doc		# Sphinx documentation
%bcond_without	tests		# unit tests
%bcond_without	python2		# Python 2.x module
%bcond_without	python3		# Python 3.x module
#
%define		module		simplejson
Summary:	Simple, fast, extensible JSON encoder/decoder for Python
Summary(pl.UTF-8):	Prosty, szybki, rozszerzalny (de)koder JSON dla Pythona
Name:		python-%{module}
Version:	3.20.1
Release:	1
License:	MIT or AFL v2.1
Group:		Libraries
#Source0Download: https://pypi.org/pypi/simplejson
Source0:	https://files.pythonhosted.org/packages/source/s/simplejson/%{module}-%{version}.tar.gz
# Source0-md5:	f4a8417d321d19b56af82d016853cbcf
URL:		https://simplejson.readthedocs.io/
%if %{with python2}
BuildRequires:	python >= 1:2.5
BuildRequires:	python-devel >= 1:2.5
BuildRequires:	python-setuptools >= 1:7
%endif
%if %{with python3}
BuildRequires:	python3 >= 1:3.3
BuildRequires:	python3-devel >= 1:3.3
BuildRequires:	python3-setuptools >= 1:7
%endif
BuildRequires:	rpm-build >= 4.6
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with doc}
BuildRequires:	sphinx-pdg-3
%endif
Requires:	python-libs >= 1:2.5
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
Requires:	python3-libs >= 1:3.3

%description -n python3-%{module}
simplejson is a simple, fast, complete, correct and extensible JSON
<http://json.org/> encoder and decoder for Python 3.

%description -n python3-%{module} -l pl.UTF-8
simplejson to prosty, szybki, pełny, poprawny i rozszerzalny koder i
dekoder JSON (<http://json.org/>) dla Pythona 3.

%package apidocs
Summary:	API documentation for Python simplejson module
Summary(pl.UTF-8):	Dokumentacja API modułu Pythona simplejson
Group:		Documentation
BuildArch:	noarch

%description apidocs
API documentation for Python simplejson module.

%description apidocs -l pl.UTF-8
Dokumentacja API modułu Pythona simplejson.

%prep
%setup -qn %{module}-%{version}

%build
%if %{with python2}
%py_build

%if %{with tests}
PYTHONPATH=$(echo $(pwd)/build-2/lib.*) \
%{__python} -m unittest discover -s build-2/lib.*/simplejson/tests
%endif
%endif

%if %{with python3}
%py3_build

%if %{with tests}
PYTHONPATH=$(echo $(pwd)/build-2/lib.*) \
%{__python3} -m unittest discover -s build-2/lib.*/simplejson/tests
%endif
%endif

%if %{with doc}
sphinx-build-3 -b html . docs/_build/html
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%{__rm} -r $RPM_BUILD_ROOT%{py_sitedir}/simplejson/tests
%py_postclean
%endif

%if %{with python3}
%py3_install

%{__rm} -r $RPM_BUILD_ROOT%{py3_sitedir}/simplejson/tests
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
%doc CHANGES.txt LICENSE.txt README.rst
%dir %{py3_sitedir}/simplejson
%{py3_sitedir}/simplejson/__pycache__
%{py3_sitedir}/simplejson/*.py
%attr(755,root,root) %{py3_sitedir}/simplejson/_speedups.cpython-*.so
%{py3_sitedir}/simplejson-%{version}-py*.egg-info
%endif

%if %{with doc}
%files apidocs
%defattr(644,root,root,755)
%doc docs/_build/html/{_static,*.html,*.js}
%endif
