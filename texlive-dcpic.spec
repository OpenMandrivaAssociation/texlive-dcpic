%global tl_name dcpic
%global tl_revision 30206

Name:		texlive-%{tl_name}
Epoch:		1
Version:	5.0.0
Release:	%{tl_revision}.1
Summary:	Commutative diagrams in a LaTeX and TeX documents
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/generic/diagrams/dcpic
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/dcpic.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/dcpic.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
DCpic is a package for typesetting Commutative Diagrams within a LaTeX
and TeX documents. Its distinguishing features are: a powerful graphical
engine, the PiCTeX package; an easy specification syntax in which a
commutative diagram is described in terms of its objects and its arrows
(morphism), positioned in a Cartesian coordinate system.

