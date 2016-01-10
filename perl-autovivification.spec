#
# Conditional build:
%bcond_with	tests		# do perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	autovivification
Summary:	autovivification - lexically disable autovivification
Summary(pl.UTF-8):	autovivification - wyłącza automatyczne ożywianie
Name:		perl-autovivification
Version:	0.16
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-authors/id/V/VP/VPIT/%{pdir}-%{version}.tar.gz
# Source0-md5:	7e20817f6034910c1bc23351d81a0658
URL:		http://search.cpan.org/dist/autovivification/
BuildRequires:	perl-ExtUtils-MakeMaker >= 6.24-2
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
When an undefined variable is dereferenced, it gets silently
upgraded to an array or hash reference (depending of the type of
the dereferencing). This behaviour is called autovivification and
usually does what you mean (e.g. when you store a value) but it
may be unnatural or surprising because your variables gets
populated behind your back. This is especially true when several
levels of dereferencing are involved, in which case all levels
are vivified up to the last, or when it happens in intuitively
read-only constructs like exists.

This pragma lets you disable autovivification for some constructs
and optionally throws a warning or an error when it would have
happened.

%description -l pl.UTF-8
Podczas odwołania do zmiennej, która nie jest zdefiniowana, zostaje
ona utworzona jako referencja do tablicy lub hasza (w zależności
od sposobu dostępu). Takie zachowanie nazywane jest automatycznym
ożywianiem i zazwyczaj robi to czego można się spodziewać
(np. wtedy gdy zapisujemy jakąś wartość), jednak może
wydawać się nienaturalnym lub zaskakującym ponieważ zmienne
same się pojawiają. Jest to szczególnie zauważalne gdy
następuje dereferencja wielopoziomowej struktury lub w przypadku,
który intuicyjnie wydaje się nie modyfikować danych, jak
np. przy użyciu exists.

Ten moduł pozwala wyłączyć automatyczne ożywianie dla
niektórych konstrukcji i opcjonalnie generować ostrzeżenie lub
błąd gdy takowe zachodzi.

%prep
%setup -q -n %{pdir}-%{version}

%build
%{__perl} -MExtUtils::MakeMaker -e 'WriteMakefile(NAME=>"%{pdir}")' \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{perl_archlib}/perllocal.pod
rm -f $RPM_BUILD_ROOT%{perl_vendorarch}/auto/autovivification/.packlist

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%dir %{perl_vendorarch}/auto/autovivification
%attr(755,root,root) %{perl_vendorarch}/auto/autovivification/autovivification.so
%{perl_vendorarch}/autovivification.pm
%{_mandir}/man3/*
