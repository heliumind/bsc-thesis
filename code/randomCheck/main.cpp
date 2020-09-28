#include <chrono>
#include <random>
#include <fstream>
#include <filesystem>
#include "json.hpp"

#define REP_COUNT 1000000

using json = nlohmann::json;
namespace fs = std::filesystem;

void saveJson(json jsonObject, fs::path fileName)
{
    std::ofstream jsonFile(fileName.string(), std::ios::out | std::ios::trunc);
    if (jsonFile.is_open())
    {
        jsonFile << jsonObject.dump();
    }
    jsonFile.close();
}

int main()
{
    unsigned seed = std::chrono::system_clock::now().time_since_epoch().count();
    std::default_random_engine generator(seed);
    std::uniform_real_distribution<double> uniDistribution(0, 1);
    std::normal_distribution<double> normDistribution(0.5, 0.2);

    json norm;
    json uni;

    for (int n = 0; n < REP_COUNT; n++)
    {
        uni.push_back(uniDistribution(generator));
        norm.push_back(normDistribution(generator));
    }

    saveJson(uni, "./uniform_distribution.json");
    saveJson(norm, "./normal_distribution.json");

    return 0;
}

