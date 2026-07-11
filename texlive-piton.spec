%global tl_name piton
%global tl_revision 79521

Name:		texlive-%{tl_name}
Epoch:		1
Version:	4.14
Release:	%{tl_revision}.1
Summary:	Typeset computer listings with LPeg of LuaLaTeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/luatex/latex/piton
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/piton.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/piton.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/piton.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package uses the Lua library LPeg to typeset and highlight computer
listings in several languages. It requires the use of LuaLaTeX. It won't
work with XeLaTeX, nor pdfLaTeX.

