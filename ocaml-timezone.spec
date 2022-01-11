#
# Conditional build:
%bcond_without	ocaml_opt	# native optimized binaries (bytecode is always built)

# not yet available on x32 (ocaml 4.02.1), update when upstream will support it
%ifnarch %{ix86} %{x8664} %{arm} aarch64 ppc sparc sparcv9
%undefine	with_ocaml_opt
%endif

Summary:	Time-zone handling
Summary(pl.UTF-8):	Obsługa stref czasowych
Name:		ocaml-timezone
Version:	0.14.0
Release:	1
License:	MIT
Group:		Libraries
#Source0Download: https://github.com/janestreet/timezone/tags
Source0:	https://github.com/janestreet/timezone/archive/v%{version}/timezone-%{version}.tar.gz
# Source0-md5:	35342e7e888a8a3c16dabef9f06f99f6
URL:		https://github.com/janestreet/timezone
BuildRequires:	ocaml >= 1:4.08.0
BuildRequires:	ocaml-core_kernel-devel >= 0.14
BuildRequires:	ocaml-core_kernel-devel < 0.15
BuildRequires:	ocaml-dune >= 2.0.0
BuildRequires:	ocaml-ppx_jane-devel >= 0.14
BuildRequires:	ocaml-ppx_jane-devel < 0.15
%requires_eq	ocaml-runtime
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		debug_package	%{nil}

%description
Timezone handles parsing timezone data and create Timezone.t that
can later be used to manipulate time in core_kernel or core.

This package contains files needed to run bytecode executables using
timezone library.

%description -l pl.UTF-8
Timezone obsługuje analizę danych stref czasowych oraz tworzenie
Timezone.t, który później można użyć do operacji na czasie w modułach
core_kernel lub core.

Pakiet ten zawiera binaria potrzebne do uruchamiania programów
używających biblioteki timezone.

%package devel
Summary:	Time-zone handling - development part
Summary(pl.UTF-8):	Obsługa stref czasowych - część programistyczna
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
%requires_eq	ocaml
Requires:	ocaml-core_kernel-devel >= 0.14
Requires:	ocaml-ppx_jane-devel >= 0.14

%description devel
This package contains files needed to develop OCaml programs using
timezone library.

%description devel -l pl.UTF-8
Pakiet ten zawiera pliki niezbędne do tworzenia programów w OCamlu
używających biblioteki timezone.

%prep
%setup -q -n timezone-%{version}

%build
dune build --verbose

%install
rm -rf $RPM_BUILD_ROOT

dune install --destdir=$RPM_BUILD_ROOT

# sources
%{__rm} $RPM_BUILD_ROOT%{_libdir}/ocaml/timezone/*.ml
# packaged as %doc
%{__rm} -r $RPM_BUILD_ROOT%{_prefix}/doc/timezone

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE.md README.md
%dir %{_libdir}/ocaml/timezone
%{_libdir}/ocaml/timezone/META
%{_libdir}/ocaml/timezone/runtime.js
%{_libdir}/ocaml/timezone/*.cma
%if %{with ocaml_opt}
%attr(755,root,root) %{_libdir}/ocaml/timezone/*.cmxs
%endif

%files devel
%defattr(644,root,root,755)
%{_libdir}/ocaml/timezone/*.cmi
%{_libdir}/ocaml/timezone/*.cmt
%{_libdir}/ocaml/timezone/*.cmti
%{_libdir}/ocaml/timezone/*.mli
%if %{with ocaml_opt}
%{_libdir}/ocaml/timezone/timezone.a
%{_libdir}/ocaml/timezone/*.cmx
%{_libdir}/ocaml/timezone/*.cmxa
%endif
%{_libdir}/ocaml/timezone/dune-package
%{_libdir}/ocaml/timezone/opam
