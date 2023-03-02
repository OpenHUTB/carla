// Copyright (c) 2023 Computer Vision Center (CVC) at the Universitat Autonoma de Barcelona (UAB). This work is licensed under the terms of the MIT license. For a copy, see <https://opensource.org/licenses/MIT>.

#pragma once

#include "CoreMinimal.h"
#include "Blueprint/UserWidget.h"

#include "USDImporterWidget.generated.h"

UCLASS()
class CARLATOOLS_API UUSDImporterWidget : public UUserWidget
{
  GENERATED_BODY()

  public:

  void ImportUSDProp(const FString& USDPath, const FString& DestinationAssetPath);
  void ImportUSDVehicle(const FString& USDPath, const FString& DestinationAssetPath);
};