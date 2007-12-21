%define realname Text-Template
%define name perl-%{realname}
%define version 1.44
%define release %mkrel 3

Summary: Text::Template module for perl
Name: %{name}
Version: %{version}
Release: %{release}
License: GPL or Artistic
Group: Development/Perl
Source: %{realname}-%{version}.tar.bz2
Url: http://search.cpan.org/dist/%{realname}/
BuildRequires: perl-devel
BuildRoot: %{_tmppath}/%{name}-buildroot/
BuildArch: noarch

%description
This is a library for generating form letters, building HTML pages, or
filling in templates generally.  A `template' is a piece of text that
has little Perl programs embedded in it here and there.  When you
`fill in' a template, you evaluate the little programs and replace
them with their values.

%prep
%setup -q -n %{realname}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make

%check
make test

%clean 
rm -rf $RPM_BUILD_ROOT

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%files
%defattr(-,root,root)
%doc Artistic COPYING README
%{perl_vendorlib}/Text
%{_mandir}/*/*


