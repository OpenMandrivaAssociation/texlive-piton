Name:		texlive-piton
Version:	70029
Release:	1
Summary:	Typeset Python listings with LPEG
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/piton
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/piton.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/piton.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/piton.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package uses the Lua library LPEG to typeset and highlight
Python listings.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/lualatex/piton
%{_texmfdistdir}/tex/lualatex/piton
%doc %{_texmfdistdir}/doc/lualatex/piton

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
