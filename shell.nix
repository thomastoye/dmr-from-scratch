{ nixpkgs ? import (fetchTarball https://github.com/NixOS/nixpkgs/archive/nixos-unstable.tar.gz) {} }:
with nixpkgs;

let
  plotextLib = pkgs.python39Packages.buildPythonPackage rec {
    pname = "plotext";
    version = "3.1.3";

    src = pkgs.python39Packages.fetchPypi {
      inherit pname version;
      sha256 = "07wdwn6rc9snfm95svsv0sqyzlhdqsif1v23wbc60qk023rcv5lz";
    };

    doCheck = false;
  };

  customPython = python39.buildEnv.override {
    extraLibs = [
      python39Packages.notebook
      python39Packages.jupyter
      python39Packages.scipy
      python39Packages.numpy
      python39Packages.matplotlib
      python39Packages.pytest
      python39Packages.pytest-watch
      # python39Packages.nbdime
      python39Packages.black
      plotextLib
    ];
  };
in
  pkgs.mkShell {
    buildInputs = [
      customPython
      git-lfs
      gnumake
    ];
  }
