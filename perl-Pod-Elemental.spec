%define upstream_name    Pod-Elemental
%define upstream_version 0.103000

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	1

Summary:	A Pod =command element
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Pod/Pod-Elemental-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Encode)
BuildRequires:	perl(Mixin::Linewise::Readers)
BuildRequires:	perl(Moose)
BuildRequires:	perl(Moose::Autobox)
BuildRequires:	perl(MooseX::Types)
BuildRequires:	perl(Pod::Eventual::Simple)
BuildRequires:	perl(String::RewritePrefix)
BuildRequires:	perl(String::Truncate)
BuildRequires:	perl(Sub::Exporter::ForMethods)
BuildRequires:	perl(Test::Deep)
BuildRequires:	perl(Test::Differences)
BuildRequires:	perl(namespace::autoclean)

BuildArch:	noarch

%description
This is a test. How many times do I need to tell you that?

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes LICENSE README
%{_mandir}/man3/*
%{perl_vendorlib}/*


%changelog
* Sat Apr 16 2011 Funda Wang <fwang@mandriva.org> 0.102.360-2mdv2011.0
+ Revision: 653617
- rebuild for updated spec-helper

* Sat Aug 28 2010 Jérôme Quelin <jquelin@mandriva.org> 0.102.360-1mdv2011.0
+ Revision: 573801
- update to 0.102360

* Tue Jul 13 2010 Jérôme Quelin <jquelin@mandriva.org> 0.101.620-1mdv2011.0
+ Revision: 552589
- update to 0.101620

* Fri Jan 22 2010 Jérôme Quelin <jquelin@mandriva.org> 0.100.220-1mdv2010.1
+ Revision: 494996
- update to 0.100220

* Sun Nov 29 2009 Jérôme Quelin <jquelin@mandriva.org> 0.93.280-1mdv2010.1
+ Revision: 471055
- update to 0.093280

* Fri Nov 06 2009 Jérôme Quelin <jquelin@mandriva.org> 0.93.0-1mdv2010.1
+ Revision: 461739
- import perl-Pod-Elemental


* Fri Nov 06 2009 cpan2dist 0.093000-1mdv
- initial mdv release, generated with cpan2dist



