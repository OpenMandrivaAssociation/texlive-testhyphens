Name:		texlive-testhyphens
Version:	38928
Release:	1
Summary:	Testing hyphenation patterns
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/testhyphens
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/testhyphens.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/testhyphens.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/testhyphens.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package may be used for testing hyphenation patterns or for
controlling that specific words are hyphenated as expected.
This package implements some old TUGboat code to adapt it to
LaTeX with some enhancements. It differs form \showhyphens,
because it typesets its output on the document's output file.
It also works with xelatex, where \showhyphens requires a
workaround.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/testhyphens
%{_texmfdistdir}/tex/latex/testhyphens
%doc %{_texmfdistdir}/doc/latex/testhyphens

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
