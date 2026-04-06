export default async function handler(req, res) {
  const { num } = req.query;

  if (!num) {
    return res.status(400).json({ error: "Number required" });
  }

  try {
    // Free API (numverify alternative)
    const response = await fetch(`http://apilayer.net/api/validate?access_key=YOUR_API_KEY&number=${num}`);
    const data = await response.json();

    return res.status(200).json({
      number: num,
      valid: data.valid,
      country: data.country_name,
      location: data.location,
      carrier: data.carrier,
      line_type: data.line_type
    });

  } catch (err) {
    return res.status(500).json({ error: "API failed" });
  }
}