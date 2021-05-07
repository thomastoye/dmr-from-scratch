{ pkgs ? import <nixpkgs> {} }:

let
  customPython = pkgs.python38.buildEnv.override {
    extraLibs = [
      pkgs.python38Packages.notebook
      pkgs.python38Packages.jupyter
    ];
  };
in

pkgs.mkShell {
  buildInputs = [ customPython ];
}

