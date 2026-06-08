function submitMode1() {
  const data = {
    crop: document.getElementById("crop").value,
    N: Number(document.getElementById("n").value),
    P: Number(document.getElementById("p").value),
    K: Number(document.getElementById("k").value),
    ph: Number(document.getElementById("ph").value)
  };

  fetch("/mode1", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(data)
  })
  .then(res => res.json())
  .then(out => {
    document.getElementById("result").innerHTML =
      `<b>Ideal Values</b><br>
       N: ${out.ideal.N}, P: ${out.ideal.P}, K: ${out.ideal.K}<br><br>
       <b>Fertilizer Needed</b><br>
       ${JSON.stringify(out.fertilizer)}`;
  });
}

function submitMode2() {
  const data = {
    N: Number(n.value),
    P: Number(p.value),
    K: Number(k.value),
    temperature: Number(temperature.value),
    humidity: Number(humidity.value),
    ph: Number(ph.value),
    rainfall: Number(rainfall.value)
  };

  fetch("/mode2", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(data)
  })
  .then(res => res.json())
  .then(out => {
    document.getElementById("result").innerHTML =
      `<b>Recommended Crop:</b> ${out.crop}`;
  });
}
