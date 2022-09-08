---
title: "file examples/libMathematicaTest.m"

description: "[No description available]"

---

# file examples/libMathematicaTest.m

[No description available]

## Attributes

|                | Name           |
| -------------- | -------------- |
| (*) ::Package(*) ::Section(*) Dummy(*) author(*) t dat)[var_] | **[CalculateSquare](/documentation/code/files/libmathematicatest_8m/)**  |
| CalculateSum[var1_, var2_] | **[__pad0__](/documentation/code/files/libmathematicatest_8m/)**  |
| | **[Var2](/documentation/code/files/libmathematicatest_8m/)**  |
| PrintVar[] | **[__pad1__](/documentation/code/files/libmathematicatest_8m/)**  |
| PrintVarorVar2[check_] | **[__pad2__](/documentation/code/files/libmathematicatest_8m/)**  |
| PrintVarorVar2[check_] | **[Var](/documentation/code/files/libmathematicatest_8m/)**  |
| VarEqualVar2[] | **[__pad3__](/documentation/code/files/libmathematicatest_8m/)**  |
| VarEqualVar2[]<>[var] | **[ToString](/documentation/code/files/libmathematicatest_8m/)**  |
| VoidTest[] | **[__pad4__](/documentation/code/files/libmathematicatest_8m/)**  |
| ExtractElement[list_, i_] | **[__pad5__](/documentation/code/files/libmathematicatest_8m/)**  |
| ExtractElement[list_, i_][var_] | **[func](/documentation/code/files/libmathematicatest_8m/)**  |



## Attributes Documentation

### variable CalculateSquare

```
(*) ::Package(*) ::Section(*) Dummy(*) author(*) t dat)[var_] CalculateSquare;
```


### variable __pad0__

```
CalculateSum[var1_, var2_] __pad0__;
```


### variable Var2

```
Var2 =2.5;
```


### variable __pad1__

```
PrintVar[] __pad1__;
```


### variable __pad2__

```
PrintVarorVar2[check_] __pad2__;
```


### variable Var

```
PrintVarorVar2[check_] Var;
```


### variable __pad3__

```
VarEqualVar2[] __pad3__;
```


### variable ToString

```
VarEqualVar2[]<>[var] ToString;
```


### variable __pad4__

```
VoidTest[] __pad4__;
```


### variable __pad5__

```
ExtractElement[list_, i_] __pad5__;
```


### variable func

```
ExtractElement[list_, i_][var_] func {i,Length[list]}]


\[Delta]var = 75;
```



## Source code

```
(* ::Package:: *)

(* ::Section:: *)
(* Dummy Mathematica package for testing *)


(* \author Tomas Gonzalo *)
(*         t.e.gonzalo@fys.uio.no *)
(* \date 2016 Sept *)



CalculateSquare[var_] := var^2;


CalculateSum[var1_,var2_]:=var1+var2


Var=42;


Var2=2.5;


PrintVar[]:=Var;


PrintVarorVar2[check_]:=If[check,Var,Var2];


VarEqualVar2[]:=Var==Var2


StringTest[var_]:="This is not a test, "<>ToString[var];


VoidTest[]:=Var=Var+1;


ExtractElement[list_,i_]:=list[[i]]


SquareList[list_]:=Table[list[[i]]^2,{i,Length[list]}]


\[Delta]var = 75;


\[CapitalGamma]func[var_] := var + 2;
```


-------------------------------

Updated on 2022-09-08 at 01:05:23 +0000
