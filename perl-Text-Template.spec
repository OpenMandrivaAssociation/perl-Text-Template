%define upstream_name    Text-Template
%define upstream_version 1.45

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    Text::Template module for perl
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}/
Source:     http://www.cpan.org/modules/by-module/Text/%{upstream_name}-%{upstream_version}.tar.bz2

BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
This is a library for generating form letters, building HTML pages, or
filling in templates generally.  A `template' is a piece of text that
has little Perl programs embedded in it here and there.  When you
`fill in' a template, you evaluate the little programs and replace
them with their values.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

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
