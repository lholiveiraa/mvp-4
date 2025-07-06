import { useState } from 'react';
import { Card, CardContent } from "../components/ui/card";
import { Button } from "../components/ui/button";
import { Input } from "../components/ui/input";
import { Label } from "../components/ui/label";


export default function HeartPredictionForm() {
  const [formData, setFormData] = useState({
    Age: '', RestingBP: '', Cholesterol: '', FastingBS: '',
    MaxHR: '', Oldpeak: '', Sex: '', ChestPainType: '',
    RestingECG: '', ExerciseAngina: '', ST_Slope: ''
  });
  const [result, setResult] = useState(null);

  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    const apiUrl = import.meta.env.VITE_API_URL || ''
    const response = await fetch(`${apiUrl}/predict`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        ...formData,
        Age: Number(formData.Age),
        RestingBP: Number(formData.RestingBP),
        Cholesterol: Number(formData.Cholesterol),
        FastingBS: Number(formData.FastingBS),
        MaxHR: Number(formData.MaxHR),
        Oldpeak: parseFloat(formData.Oldpeak)
      })
    });
    const data = await response.json();
    setResult(data.prediction);
  };

  return (
    <Card className="max-w-2xl mx-auto mt-10 p-6 shadow-2xl rounded-2xl">
      <CardContent>
        <h1 className="text-2xl font-bold mb-6 text-center">Predição de Doença Cardíaca</h1>
        <form className="grid grid-cols-2 gap-4" onSubmit={handleSubmit}>
          {Object.keys(formData).map((key) => (
            <div key={key} className="flex flex-col">
              <Label htmlFor={key}>{key}</Label>
              <Input
                id={key}
                name={key}
                value={formData[key]}
                onChange={handleChange}
                required
              />
            </div>
          ))}
          <div className="col-span-2 flex justify-center">
            <Button type="submit" className="w-1/2">Enviar</Button>
          </div>
        </form>
        {result !== null && (
          <div className="mt-6 text-center text-lg font-semibold">
            Resultado: {result === 1 ? "Com doença cardíaca" : "Sem doença cardíaca"}
          </div>
        )}
      </CardContent>
    </Card>
  );
}
