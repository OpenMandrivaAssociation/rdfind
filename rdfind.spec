Name: rdfind
Version: 1.6.0
Release: 1
Source0: https://rdfind.pauldreik.se/rdfind-%{version}.tar.gz
Summary: Utility for finding duplicate files
URL: https://github.com/pauldreik/rdfind
# Also https://rdfind.pauldreik.se/
License: GPL-2.0
Group: System

%description
Rdfind is a program that finds duplicate files. It is useful for compressing
backup directories or just finding duplicate files. It compares files based
on their content, NOT on their file names.

%prep
%autosetup -p1
%configure

%build
%make_build

%install
%make_install

%files
%{_bindir}/rdfind
%{_mandir}/man1/rdfind.1*
