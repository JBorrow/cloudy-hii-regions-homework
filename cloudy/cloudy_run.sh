module purge
module load cloudy

mkdir temp_var_lowdensity
mkdir temp_var_highdensity
mkdir dens_var
mkdir dens_var_only_hydrogen
mkdir qh_var

cd temp_var_lowdensity

for temp in 10000 20000 30000 40000 50000 60000 70000 80000 90000 100000
do
    echo "lowdensity ${temp}"
    mkdir $temp
    cd $temp
    cp ../../hii_coolstar.in .
    sed -i "s/replace-me-temp/${temp}/" hii_coolstar.in
    sed -i "s/replace-me-dens/1/" hii_coolstar.in
    sed -i "s/replace-me-qh/49/" hii_coolstar.in
    cloudy.exe -r hii_coolstar
    cd ..
done

cd ../temp_var_highdensity

for temp in 10000 20000 30000 40000 50000 60000 70000 80000 90000 100000
do
    echo "highdensity ${temp}"
    mkdir $temp
    cd $temp
    cp ../../hii_coolstar.in .
    sed -i "s/replace-me-temp/${temp}/" hii_coolstar.in
    sed -i "s/replace-me-dens/3/" hii_coolstar.in
    sed -i "s/replace-me-qh/49/" hii_coolstar.in
    cloudy.exe -r hii_coolstar
    cd ..
done

cd ../dens_var

for dens in {1..5}
do
    echo "density ${dens}"
    mkdir $dens
    cd $dens
    cp ../../hii_coolstar.in .
    sed -i "s/replace-me-temp/35000/" hii_coolstar.in
    sed -i "s/replace-me-dens/${dens}/" hii_coolstar.in
    sed -i "s/replace-me-qh/49/" hii_coolstar.in
    cloudy.exe -r hii_coolstar
    cd ..
done

cd ../qh_var

for qh in {47..52}
do
    echo "qh ${qh}"
    mkdir $qh
    cd $qh
    cp ../../hii_coolstar.in .
    sed -i "s/replace-me-temp/35000/" hii_coolstar.in
    sed -i "s/replace-me-dens/2/" hii_coolstar.in
    sed -i "s/replace-me-qh/${qh}/" hii_coolstar.in
    cloudy.exe -r hii_coolstar
    cd ..
done

cd ../dens_var_only_hydrogen

for dens in {1..5}
do
    echo "density only H ${dens}"
    mkdir $dens
    cd $dens
    cp ../../hii_only_hydrogen.in .
    sed -i "s/replace-me-temp/35000/" hii_only_hydrogen.in
    sed -i "s/replace-me-dens/${dens}/" hii_only_hydrogen.in
    cloudy.exe -r hii_only_hydrogen
    cd ..
done

