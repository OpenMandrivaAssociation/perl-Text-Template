%define upstream_name    Text-Template
%define upstream_version 1.45

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	Text::Template module for perl
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}/
Source:		http://www.cpan.org/modules/by-module/Text/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:	perl-devel
BuildRequires:	perl-JSON-PP
BuildArch:	noarch

%description
This is a library for generating form letters, building HTML pages, or
filling in templates generally.  A `template' is a piece of text that
has little Perl programs embedded in it here and there.  When you
`fill in' a template, you evaluate the little programs and replace
them with their values.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
make

%check
make test

%install
%makeinstall_std

%files
%doc Artistic COPYING README
%{perl_vendorlib}/Text
%{_mandir}/*/*


%changelog
* Mon Aug 03 2009 Jérôme Quelin <jquelin@mandriva.org> 1.450.0-1mdv2010.0
+ Revision: 408089
- rebuild using %%perl_convert_version

* Fri Aug 08 2008 Thierry Vignaud <tvignaud@mandriva.com> 1.45-2mdv2009.0
+ Revision: 268830
- rebuild early 2009.0 package (before pixel changes)

* Mon Apr 21 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.45-1mdv2009.0
+ Revision: 196170
- update to new version 1.45
- update to new version 1.45

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 1.44-3mdv2008.1
+ Revision: 136362
- restore BuildRoot

  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill re-definition of %%buildroot on Pixel's request


* Sun Jan 14 2007 Olivier Thauvin <nanardon@mandriva.org> 1.44-3mdv2007.0
+ Revision: 108448
- rebuild

  + Guillaume Rousse <guillomovitch@mandriva.org>
    - Import perl-Text-Template

* Wed Jan 26 2005 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 1.44-3mdk
- Rebuild
- Remove dependency on perl

