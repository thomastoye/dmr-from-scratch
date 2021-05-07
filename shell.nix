{ pkgs ? import <nixpkgs> {} }:

let
  commpy = pkgs.python38Packages.buildPythonPackage rec {
      pname = "scikit-commpy";
      version = "0.6.0";

      src = pkgs.python38Packages.fetchPypi{
        inherit version;
        inherit pname;
        sha256 = "1n5i5fdglg9s1lyr2rx72h742ighl97llznw3ksbazmxrcs7zv1r";
      };

      doCheck = false;

      buildInputs = [
        pkgs.python38Packages.numpy
        pkgs.python38Packages.scipy
        pkgs.python38Packages.matplotlib
        pkgs.python38Packages.nose
        pkgs.python38Packages.sympy
      ];
    };
  customPython = pkgs.python38.buildEnv.override {
    extraLibs = [
      pkgs.python38Packages.notebook
      pkgs.python38Packages.jupyter
      pkgs.python38Packages.scipy
      pkgs.python38Packages.numpy
      pkgs.python38Packages.matplotlib
      commpy
      pkgs.python38Packages.nbdime
    ];
  };
in
  pkgs.mkShell {
    buildInputs = [
      customPython
      pkgs.git-lfs
    ];
  }

