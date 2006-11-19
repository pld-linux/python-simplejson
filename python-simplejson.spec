# $Revision: 1.1 $
%define     module  simplejson
Summary:	Simple, fast, extensible JSON encoder/decoder for Python
Summary(pl):	Prosty, szybki, rozszerzalny (de)koder JSON dla Pythona
Name:		python-%{module}
Version:	1.4
Release:	0.1
License:	MIT
Group:		Libraries
Source0:    http://cheeseshop.python.org/packages/source/s/%{module}/%{module}-%{version}.tar.gz
# Source0-md5:	5fbad786a4b151d44a9b1e1e157e5510
URL:		http://undefined.org/python/#simplejson
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
simplejson is a simple, fast, complete, correct and extensible JSON
<http://json.org> encoder and decoder for Python 2.3+. It is pure Python
code with no dependencies.

%prep
%setup -qn %{module}-%{version}

%build
python setup.py build
	
%install
rm -rf $RPM_BUILD_ROOT

python setup.py install \
	--root=$RPM_BUILD_ROOT \
	--optimize=2
	
%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{py_sitescriptdir}/%{module}
%{py_sitescriptdir}/%{module}/*.py[co]
