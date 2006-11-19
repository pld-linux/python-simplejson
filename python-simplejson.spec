# $Revision: 1.5 $
%define		module		simplejson
Summary:	Simple, fast, extensible JSON encoder/decoder for Python
Summary(pl):	Prosty, szybki, rozszerzalny (de)koder JSON dla Pythona
Name:		python-%{module}
Version:	1.4
Release:	0.3
License:	MIT
Group:		Libraries
Source0:	http://cheeseshop.python.org/packages/source/s/simplejson/%{module}-%{version}.tar.gz
# Source0-md5:	5fbad786a4b151d44a9b1e1e157e5510
URL:		http://undefined.org/python/#simplejson
BuildRequires:	python >= 1:2.5
BuildRequires:	rpm-pythonprov
%pyrequires_eq	python-libs
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
simplejson is a simple, fast, complete, correct and extensible JSON
<http://json.org/> encoder and decoder for Python 2.3+. It is pure
Python code with no dependencies.

%description -l pl
simplejson to prosty, szybki, pe³ny, poprawny i rozszerzalny koder i
dekoder JSON (<http://json.org/>) dla Pythona 2.3 i nowszych wersji.
Jest to kod wy³±cznie w Pythonie bez dodatkowych zale¿no¶ci.

%prep
%setup -qn %{module}-%{version}

%build
python setup.py build
	
%install
rm -rf $RPM_BUILD_ROOT

python setup.py install \
	--root=$RPM_BUILD_ROOT \
	--optimize=2

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{py_sitescriptdir}/json
%{py_sitescriptdir}/json/*.py[co]
%{py_sitescriptdir}/json-%{version}-py*.egg-info
