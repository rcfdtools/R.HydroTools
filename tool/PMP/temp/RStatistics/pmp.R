#CURSO HIDG by r.cfdtools@gmail.com
#Licencia, cláusulas y condiciones de uso en: https://bit.ly/3bBmgca
#Distributions: 1-Normal, 2-Gumbel, 3-LogGumbel, 4-LogPearsonIII
#Tested with R 3.6.0 https://www.r-project.org/
#Tested with RTools 3.5 https://cran.r-project.org/bin/windows/Rtools/
#Tested in RStudio 1.2.1335 https://www.rstudio.com/
#Tested with MiKTeX 2.9.7076 https://miktex.org/about
#Requiere: library(readxl), require(rriskDistributions)

##### FUNCIONES GENERALES #####

#FUNCIÓN: Gráficas de la estación seleccionada
fStationEvalAll <- function(x,vStationName){
  vGraphTitle <- paste("Resumen Estadístico (Id: ",vStationName,")")
  cat ("\n-------------------------------------\n",vGraphTitle,"\n-------------------------------------\n")
  print(summary(x))     #Estadísticos descriptivos generales  
  vGraphTitle <- paste("Histograma (Id: ",vStationName,")")
  cat ("\n-------------------------------------\n",vGraphTitle,"\n-------------------------------------\n")
  h <- hist(x, cex.main=vGrphTitSize, main = vGraphTitle)
  print (h)
  vGraphTitle <- paste("BoxPlot (Id: ",vStationName,")")
  cat ("\n-------------------------------------\n",vGraphTitle,"\n-------------------------------------\n")
  bpt <- boxplot(x, notch=vShowBoxPlotNotch, cex.main=vGrphTitSize, main = vGraphTitle);
  print (bpt)
  vGraphTitle <- paste("Densidad (Id: ",vStationName,")")
  #if (vStationEvalAll == FALSE){
    cat ("\n-------------------------------------\n",vGraphTitle,"\n-------------------------------------\n")
    dst <- density(x)
    print (dst)
    plot(density(x), cex.main=vGrphTitSize, main = vGraphTitle)
  #}
}

#FUNCIÓN: Tablas y gráficas combinadas
fStationGraphTableMix <- function(vStationName){
  #Value Table
  cat("\n")
  print(data.frame(Tr, pt, W, z, XTrDNormal, XTrDGumbel, XTrDLogGumbel))
  vMaxXTrAux <<- max(vMaxXTr)
  vMinXTrAux <<- min(vMinXTr)
  
  #Grafica general de distribucion de todas las estaciones
  vGraphTitle <- paste("Probability Distributions (Id: ",vStationName,")")
  plot(x, P_E, ylim=c(0,1), pch=1, cex=0.75, col="blue", bg="#FF6666", type="l", lty=1, lwd=1.5,
       ylab = "Cumulative Probability", xlab = "x", 
       cex.main=vGrphTitSize, main = vGraphTitle)
  if (fDistNormalOn == TRUE) {lines(x, F_DNormal, pch=2, cex=0.75, type="b", lty=2, col="black", lwd=0.5)}
  if (fDistGumbelOn == TRUE) {lines(x, F_DGumbel, pch=3, cex=0.75, type="b", lty=3, col="black", lwd=1)}
  if (fDistLogGumbelOn == TRUE) {lines(x, F_DLogGumbel, pch=4, cex=0.75, type="b", lty=4, col="black", lwd=1)}
  if (fDistLogPearsonIIIOn == TRUE) {lines(x, F_DLogPearsonIII, pch=5, cex=0.75, type="b", lty=5, col="black", lwd=1)}
  grid( )
  legend("bottomright", legend=c("Empirical Distribution", "Normal", "Gumbel", "Log-Gumbel", "Log Pearson III"),
         lty=1:4, col=c("blue", "black", "black", "black", "black"), bg="white", pch=1:5, cex=0.75, text.font=3, title= "r.cfdtools@gmail.com")
  
  ##Grafica general de valores estimados de todas las estaciones
  vGraphTitle <- paste("XTr vs Return period (Id: ",vStationName,")")
  plot(Tr, XTrDNormal, ylim=c(vMinXTrAux,vMaxXTrAux), pch=1, cex=0.75, col="black", bg="#FF6666", type="b", lty=1, lwd=1,
       ylab = "XTr", xlab = "Return period (years)", 
       cex.main=vGrphTitSize, main = vGraphTitle)
  if (fDistNormalOn == TRUE) {lines(Tr, XTrDNormal, pch=1, cex=0.75, type="b", lty=1, col="black",lwd=1)}
  if (fDistGumbelOn == TRUE) {lines(Tr, XTrDGumbel, pch=2, cex=0.75, type="b", lty=2, col="black",lwd=1)}
  if (fDistLogGumbelOn == TRUE) {lines(Tr, XTrDLogGumbel, pch=3, cex=0.75, type="b", lty=3, col="black",lwd=1)}
  grid( )
  legend("bottomright", legend=c("XTrDNormal", "XTrDGumbel", "XTrDLogGumbel"),
         lty=1:3, col=c("black", "black", "black"), bg="white", pch=1:3, cex=0.8, text.font=3, title= "r.cfdtools@gmail.com")
  
  cat("\n--------------------------------------------------\nKOLMOGOROV-SMIRNOV Delta (Id:", vStationName, ")\n--------------------------------------------------\n")
  #cat("\nKOLMOGOROV-SMIRNOV Delta (Id:", vStationName, "\n")
  cat("D.Normal: ",vDeltaKolmogorov[1],"\n")
  cat("D.Gumbel: ",vDeltaKolmogorov[2],"\n")
  cat("D.Log-Gumbel: ",vDeltaKolmogorov[3],"\n")
  cat("D.Log Pearson III: ",vDeltaKolmogorov[4],"\n")
  cat("\n--------------------------------------------------\nValor mínimo y máximo en las distribuciones\n--------------------------------------------------\n")
  print(data.frame(vMinXTrAux,vMaxXTrAux))
}

#FUNCIÓN: Prueba de bondad de ajuste usando el método de Kolmogorov-Smirnov usando una función
vDeltaKolmogorov <<- c()                        #Vector global <<- para almacenar los valores de Kolmogorov para cada distribucion
fTestKolmogorov <- function(vDistID,vP_E,vF_Dist){
  #Kolmogorov-Smirnov Test
  dFP <- abs(vP_E - vF_Dist)
  dFP <- sort(dFP, decreasing = TRUE); dFP
  delta <- dFP[1]; delta
  cat("\nTest de Kolmogorov-Smirnov")
  #Theoretical delta 
  if (n<35){
    deltao<-0.000003848186*n**4-0.00033109622*n**3+0.010220554*n**2-0.141035449935*n+1.07518805168
  } else {deltao <- 1.36/sqrt(n)
  }
  cat("\n")
  print(data.frame(delta, deltao)) #delta es mayor distancia respecto al valor teorico, deltao es valor critico de la funcion de Kolmogorov
  if (deltao > delta){
    cat("Distribution fit the curve\n")
  } else { cat("Distribution doesn’t fit the curve\n")
  }
  vDeltaKolmogorov[vDistID] <<- delta #<<- asigna variable global dentro de la funcion
}

#FUNCION: Longitud de la serie a estudiar
fSerieLen <- function(x){
  ncount <- length(x)
  n <<- 0
  for (i in 1:ncount) {if (x[i] >= 0) {n <<- n+1}} #Conteo de datos existentes, puede mostrar alerta en rojo en serie con vacios
}

#FUNCION: Ordenamiento de serie para cada estación
fSerieSort <- function(vStation){
  for(i in 1:vStationN) {                         #Buscar la estacion en la tabla de entrada
    vStationAux <- vFile[vStationName[i]]
    vStationAux <- c(vStationAux)                 #Convertir a vector c()
    #Cambio de variable X como variable estándar y ordenada de menor a mayor
    if(vStationName[i] == vStation){x <<- sort(vStationAux[[1]], decreasing = FALSE)}
    #for (i in 1:n) {cat(i,",",x[i],"\n")};       #Mostrar lista de valores ordenados de la serie
  }
}

#FUNCION: Distribución empírica propuesta por Weibull
fDistEmpWeibull <- function(n){
  P_E <- c()
  for (i in 1:n) {P_E[i] <- i / (n+1)};  
  cat("\n")
  print(data.frame(x, P_E))                     #Mostrar los valores ordenados de x y la distribucion empirica de Weibull
  P_E <<- P_E                                   #Definir P_E como global
}

#FUNCION: Distribución Normal
fDistNormal <- function(x,vStationName){
  cat("\n--------------------------------------------------\nDistribución Normal (Id:",vStationName,")\n--------------------------------------------------\n")  
  vDistID <- 1 #Distribution ID
  mu <- mean(x)
  dvstd <- sd(x)
  cat("\n")
  print(data.frame(mu, dvstd))
  F_DNormal <- c()
  for (i in 1:n) {F_DNormal[i] <- pnorm(x[i], mean=mu, sd=dvstd, lower.tail=TRUE)}
  F_DNormal <<- F_DNormal #Set as global var
  cat("\n")
  print(data.frame(x, P_E, F_DNormal))
  vGraphTitle <- paste("NORMAL DISTRIBUTION (Id: ",vStationName,")")
  #Grafica de probabilidades
  plot (x, F_DNormal, type="l", pch=20, col="red", lty=2, xlab="", ylab="Cumulative probability", cex.main=vGrphTitSize, main=vGraphTitle)
  lines (x, P_E, pch=18, col="blue", type="b", lty=1)
  grid()
  legend ("bottomright", legend=c("Normal Distribution", "Empirical Distribution"), 
          lty=1:2, col=c("red", "blue"), cex=0.8 , text.font=3, title= "r.cfdtools@gmail.com")
  #D.NORMAL>> Probabilidades y quantiles - Precipitación para diferentes periodos de retorno
  W <- c()
  W <- (log(1/pt)**2)**0.5
  W <<- W  #Set as global var
  z <- c()
  for (i in 1:nTr)
  {
    if (pt[i] <= 0.5) {
      z[i] <- (W[i]-((2.515517+0.802853*W[i]+0.010328*W[i]**2)/(1+1.432788*W[i]+0.189269*W[i]**2+0.001308*W[i]**3)))
      #cat(i,"-",pt[i],"-",W[i],"-", z[i],"\n")
      } 
    else {
      z[i] <- (1-pt[i])
      }
  }
  z <<- z #Set as global var
  XTrDNormal <- c() #Corresponde al valor estimado para cada periodo de retorno
  XTrDNormal <- mu+z*dvstd
  XTrDNormal <<- XTrDNormal #Set as global var
  vMaxXTr[1] <<- max(XTrDNormal)
  vMinXTr[1] <<- min(XTrDNormal)
  cat("\n------------------------------------------------------\n")
  cat("D.NORMAL: Probabilidades y quantiles (Id: ",vStationName ,")")
  cat("\n------------------------------------------------------\n")
  print(data.frame(Tr, pt, W, z, XTrDNormal))
  vGraphTitle <- paste("XTrDNormal vs Return period (Id: ",vStationName,")")
  plot(Tr, XTrDNormal, pch=20, col="#000099", bg="#FF6666", type="b" , lty=1, ylab = "XTrDNormal", xlab = "Return period (years)", cex.main=vGrphTitSize, main = vGraphTitle)
  grid()
  fTestKolmogorov(vDistID,P_E,F_DNormal)
}

#FUNCION: Distribución Gumbel
fDistGumbel <- function(x,vStationName){
  cat("\n--------------------------------------------------\nDistribución de Gumbel (Id:",vStationName,")\n--------------------------------------------------\n")    
  #Parameter calculation, Method o f Moments
  vDistID <- 2 #Distribution ID
  alph <- sqrt(6) * sd(x)/pi
  mu <- mean(x) - 0.57721/alph
  cat("\n")  
  print(data.frame(alph ,mu))
  F_DGumbel <- c()
  for (i in 1:n) {F_DGumbel[i] <- exp(-exp(-(x[i]-mu)/alph))}
  F_DGumbel <<- F_DGumbel #Set as global var
  cat("\n")
  print(data.frame(x, P_E, F_DGumbel))
  vGraphTitle <- paste("GUMBEL DISTRIBUTION (Id: ",vStationName,")")
  plot (x, F_DGumbel, type="l", pch=20, col="red", lty=2, xlab="", ylab="Cumulative probability", 
        cex.main=vGrphTitSize, main=vGraphTitle)
  lines (x, P_E, pch=18, col="blue", type="b", lty=1)
  grid()
  legend ("bottomright", legend=c("Gumbel Distribution", "Empirical Distribution"), 
          lty=1:2, col=c("red", "blue"), cex=0.8 , text.font=3, title= "r.cfdtools@gmail.com")
  #D.GUMBEL>> Cálculo de probabilidades y quantiles - Precipitación para diferentes periodos de retorno
  XTrDGumbel <<- mu-log((-log(p, exp(1))), exp(1)) * alph
  cat("\n")
  print(data.frame(Tr, pt, XTrDGumbel)) #Tabla de resultados
  vMaxXTr[2] <<- max(XTrDGumbel)
  vMinXTr[2] <<- min(XTrDGumbel)
  vGraphTitle <- paste("XTrDGumbel vs Return period (Id: ",vStationName,")")
  plot(Tr, XTrDGumbel, pch=20, col="#000099", bg="#FF6666", type="b" , lty=1,
       ylab = "XTrDGumbel", xlab = "Return period (years)", cex.main=vGrphTitSize,
       main = vGraphTitle)
  grid()
  fTestKolmogorov(vDistID,P_E,F_DGumbel)  
}

#FUNCION: Distribución Log-Gumbel
fDistLogGumbel <- function(x,vStationName){
  cat("\n--------------------------------------------------\nDistribución Log Gumbel (Id:",vStationName,")\n--------------------------------------------------\n")    
  #Parameter calculation, Method o f Moments
  vDistID <- 3 #Distribution ID
  alph <- sqrt(6)*sd(log(x,exp(1)))/pi
  mu <- mean(log(x,exp(1)))-0.57721*alph
  cat("\n")
  print(data.frame(alph, mu))
  F_DLogGumbel <- c()
  for (i in 1:n) {F_DLogGumbel[i] <- exp(-exp(-(log(x[i],exp(1))-mu)/alph))}
  F_DLogGumbel <<- F_DLogGumbel #Set as global var
  cat("\n")
  print(data.frame(x, P_E, F_DLogGumbel))
  vGraphTitle <- paste("LOG-GUMBEL DISTRIBUTION (Id: ",vStationName,")")
  plot(x, F_DLogGumbel, type="l", pch=20, col="red", lty=2, xlab="", ylab="Cumulative probability", 
       cex.main=vGrphTitSize, main=vGraphTitle) 
  lines (x, P_E, pch=18, col="blue", type="b", lty=1)
  grid ()
  legend("bottomright", legend=c("Log-Gumbel Distribution", "Empirical Distribution"), 
         lty=1:2, col=c("red", "blue"), cex=0.8, text.font=3, title= "r.cfdtools@gmail.com")
  #D.LOG-GUMBEL>> Cálculo de probabilidades y quantiles
  #D.LOG-GUMBEL>> Precipitación para diferentes periodos de retorno
  XTrDLogGumbel <<- exp(mu-log((-log(p,exp(1))) ,exp(1))*alph)
  cat("\n")
  print(data.frame(Tr, pt, XTrDLogGumbel))
  vMaxXTr[3] <<- max(XTrDLogGumbel)
  vMinXTr[3] <<- min(XTrDLogGumbel)
  vGraphTitle <- paste("XTrDLogGumbel vs Return period (Id: ",vStationName,")")
  plot(Tr, XTrDLogGumbel, pch=20, col="#000099", bg="#FF6666", type="b", lty=1, 
       ylab = "XTrDLogGumbel", xlab = "Return period (years)", 
       cex.main=vGrphTitSize, main = vGraphTitle)
  grid( )
  fTestKolmogorov(vDistID,P_E,F_DLogGumbel) 
}

#FUNCION: Distribución Log Pearson III
fDistLogPearsonIII <- function(x,vStationName){
  cat("\n--------------------------------------------------\nDistribución Log Pearson III (Id:",vStationName,")\n--------------------------------------------------\n")    
  #Parameter calculation, Method o f Moments
  vDistID <- 4 #Distribution ID
  #Bias to calculating the position parameter
  CSG <- n*sum(( log(x,exp(1))-mean(log(x,exp(1))))**3)/((n-1)*(n-2)*sd(log(x, exp(1)))**3)
  CSG <<- CSG  # <<<<<< check purposo - no required >>>>>>>>>
  #Position parameter(+): 
  Xo <- mean(log(x,exp(1)))-2*sd(log(x,exp(1)))/CSG
  #Form parameter (+): 
  gam <- 4/CSG**2
  #Scale Parameter (+): 
  Beta <- CSG*sd(log(x,exp(1)))/2
  cat("\n")
  print(data.frame(Xo, gam, Beta))
  #Cumulative Distribution Si se cumple con la condición: β > 0:
  DNMR <- c(gam)
  Lga <- gam*(gam+1)
  for (i in 1:(n-1))
  { 
    DNMR[i+1] <- Lga
    Lga = Lga*(gam+i+1)
  }
  #cat("\n") # <<<<<< checking purpose - no required >>>>>>>>>
  #print(data.frame(DNMR)) # <<<<<< checking purpose - no required >>>>>>>>>
  Gy <- c()
  LY <- (log(x,exp(1))-Xo)/Beta; LY
  #cat("\n") # <<<<<< checking purpose - no required >>>>>>>>>
  #print(data.frame(LY)) # <<<<<< checking purpose - no required >>>>>>>>>  
  for (i in 1:n)
  {
    NMDR <- c()
    for (j in 0:(n-1)){
      NMDR[j+1] <- LY[i]**(gam+j)}
      NMDR <<- NMDR
    if (Xo>0){Gy[i] <- (exp(-LY[i])*sum(NMDR/DNMR)/gamma(gam))}
    #if (Xo>0){Gy[i] <- (exp(-LY[i])*sum(NMDR/DNMR))}
  }; Gy
  #cat("\n") # <<<<<< checking purpose - no required >>>>>>>>>
  #print(data.frame(NMDR)) # <<<<<< checking purpose - no required >>>>>>>>>  
  #cat("\n") # <<<<<< checking purpose - no required >>>>>>>>>
  #print(data.frame(Gy)) # <<<<<< checking purpose - no required >>>>>>>>>  
  F_DLogPearsonIII <- 1-Gy #r.cfd Cambiar por 1-Gy si la grafica es mostrada en orden contrario
  F_DLogPearsonIII <<- F_DLogPearsonIII #Set as global var
  cat("\n") # <<<<<< checking purpose - no required >>>>>>>>>
  print(data.frame(F_DLogPearsonIII)) # <<<<<< checking purpose - no required >>>>>>>>>    
  #F_GM <- Gy #r.cfd
  if (NMDR[1] != Inf | is.na(NMDR[1]) == TRUE){
    vGraphTitle <- paste("LOG PEARSON III DISTRIBUTION (Id: ",vStationName,")")
    plot(x, F_DLogPearsonIII, type="l", pch=20, col="red", lty=2, xlab="", ylab="Cumulative probability", cex.main=vGrphTitSize, main=vGraphTitle)
    lines (x, P_E, pch=18, col="blue", type="b", lty=1)
    legend( "bottomright", legend=c( "Log−Pearson III Distribution", "Empirical Distribution"), 
            lty=1:2, col=c("red", "blue"), cex=0.8, text.font=3, title= "r.cfdtools@gmail.com")
    grid()
    cat("\n--------------------------------------------------\nLog Pearson III\n--------------------------------------------------\n")
    fTestKolmogorov(vDistID,P_E,F_DLogPearsonIII)
  }
}

##### LLAMADO DE DATOS Y DEFINICION DE VARIABLES GLOBALES #####
vStation <<- '25020230'                             #ID de la estacion única a estudiar Ej: a25020230 o Zonal
vStationEvalAll <<- F                           #Mostrar datos y graficas estadísticas de cada estación, T-True, F-False, no usar comillas
vShowBoxPlotNotch <- F                          #Mostrar muescas en graficas BoxPlot, T-True, F-False, no usar comillas
fDistNormalOn <<- T                             #Activar la Distribución Normal, T-True or F-False
fDistGumbelOn <<- T                             #Activar la Distribución Gumbel, T-True or F-False
fDistLogGumbelOn <<- T                          #Activar la Distribución LogGumbel, T-True or F-False
fDistLogPearsonIIIOn <<- T                      #Activar la Distribución LogPearsonIII, T-True or F-False
setwd("D:\\R.GISPython\\PMP\\old\\R") #Directorio de trabajo  
library(readxl)                                 #Librería apaertura de archivos de Excel
#Abrir el Libro de Excel indicando el rango de columnas a utilizar excluyendo la columna A del año
vFile <- read_excel("25020230.xlsx", 
         sheet="PMax24Hr", 
         col_names = TRUE, 
         range = cell_cols("B:B"))
vFile                                           #Ver resumen del archivo cargado
#View(vFile)                                    #Ver el contenido del archivo de datos en nueva ventana
attach(vFile)                                   #Agregar el archivo a la ruta de busqueda
vStationName <- c(names(vFile))                 #Guardar los nombres de las estaciones un vector
data.frame(vStationName)                        #Mostrar los nombres de las estaciones
vStationN <- length(vStationName)               #Numero de series contenidas en el archivo
#vStationNameA <- vStationName[c(2:vStationN)]  #Listado de series sin incluir el Año de la primer columna
vStationTxt <- vStation                         #Etiqueta para graficos Ej: a25020230 o Zonal
vMaxXTr <<- c()                                 #Vector para almacenar máximos estimados para ajuste plot
vMinXTr <<- c()                                 #Vector para almacenar mínimos estimados para ajuste plot
#fSerieSort(vStation)                              #Buscar la estacion en la tabla de entrada y ordenar la serie

#Periodos de retorno y probabilidades
Tr <- c(2, 2.33, 3, 5, 10, 15, 20, 25, 
        50, 75, 100, 200, 250, 500, 1000)       #Tr, Periodos de retorno en años
nTr <- length(Tr)                               #Longitud de la serie a estudiar
p <- 1-1/Tr                                     #P≤, Probabilidades menores que, para cada Tr
pt <- 1/Tr                                      #P≥, Probabilidades mayores que, para cada Tr

#Grafica general de todas las estaciones
vGrphTitSize <- 0.9                             #Tamaño del título en las gráficas
boxplot(vFile, notch=vShowBoxPlotNotch, horizontal=FALSE, las=2, cex.main=vGrphTitSize, main="Boxplot, todas las estaciones")

#Gráficas y tablas para cada estación cuando se ha definido vStationEvalAll = T
if (vStationEvalAll == TRUE) {
  for(i in 1:vStationN) {
    fSerieSort(vStationName[i])                   #Buscar la estacion en la tabla de entrada y ordenar la serie
    fSerieLen(x)                                  #Longitud de la serie a estudiar, cálculo  
    fDistEmpWeibull(n)
    vStationAux1 <- vFile[vStationName[i]]
    vStationAux1 <- c(vStationAux1)
    cat("\n-------------------------------------\n Datos (Id: ",vStationName[i],")\n-------------------------------------\n")
    print(data.frame(vStationAux1[[1]]))
    #fStationEvalAll(vStationAux1[[1]],vStationName[i])
    fStationEvalAll(x,vStationName[i])
    if (fDistNormalOn == TRUE) {fDistNormal(x,vStationName[i])}
    if (fDistGumbelOn == TRUE) {fDistGumbel(x,vStationName[i])}
    if (fDistLogGumbelOn == TRUE) {fDistLogGumbel(x,vStationName[i])}
    if (fDistLogPearsonIIIOn == TRUE) {fDistLogPearsonIII(x,vStationName[i])}
    fStationGraphTableMix(vStationName[i])
  }
} else {
    fSerieSort(vStation)                        #Buscar la estacion en la tabla de entrada y ordenar la serie
    fSerieLen(x)                                #Longitud de la serie a estudiar, cálculo
    fDistEmpWeibull(n)
    cat("\n-------------------------------------\n",vStation,"\n-------------------------------------\n")
    fStationEvalAll(x,vStation)
    if (fDistNormalOn == TRUE) {fDistNormal(x,vStation)}
    if (fDistGumbelOn == TRUE) {fDistGumbel(x,vStation)}
    if (fDistLogGumbelOn == TRUE) {fDistLogGumbel(x,vStation)}
    if (fDistLogPearsonIIIOn == TRUE) {fDistLogPearsonIII(x,vStation)}
    fStationGraphTableMix(vStation)
}


##### ANALISIS DE VARIAS DISTRIBUCIONES USANDO LA LIBRERIA rriskDistributionsL #####
#installed.packages("rriskDistributions")
#require(rriskDistributions)
#vAjuste <- fit.cont(x)
