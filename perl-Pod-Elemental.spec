%define upstream_name    Pod-Elemental
%define upstream_version 0.093280

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    A Pod =command element
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Pod/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Encode)
BuildRequires: perl(Mixin::Linewise::Readers)
BuildRequires: perl(Moose)
BuildRequires: perl(Moose::Autobox)
BuildRequires: perl(MooseX::Types)
BuildRequires: perl(Pod::Eventual::Simple)
BuildRequires: perl(String::RewritePrefix)
BuildRequires: perl(String::Truncate)
BuildRequires: perl(Sub::Exporter::ForMethods)
BuildRequires: perl(Test::Deep)
BuildRequires: perl(Test::Differences)
BuildRequires: perl(namespace::autoclean)
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
This is a test. How many times do I need to tell you that?

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor

%{make}

%check
%{make} test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes LICENSE README
%{_mandir}/man3/*
%perl_vendorlib/*


